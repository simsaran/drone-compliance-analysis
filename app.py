import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
from pathlib import Path

st.set_page_config(
    page_title="Transport Canada Drone Compliance",
    page_icon="🚁",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .block-container{padding:1.5rem 2rem}
    .kpi{background:white;border-radius:12px;padding:16px 20px;border:1px solid #E8E8E8;box-shadow:0 1px 4px rgba(0,0,0,0.05);margin-bottom:8px}
    .kpi-label{font-size:11px;color:#888;margin-bottom:4px;font-weight:500;text-transform:uppercase;letter-spacing:.04em}
    .kpi-value{font-size:26px;font-weight:700;color:#111;line-height:1.1}
    .kpi-note{font-size:11px;color:#888;margin-top:3px}
    .kpi-red .kpi-value{color:#C0392B}
    .kpi-green .kpi-value{color:#0A7540}
    .kpi-amber .kpi-value{color:#B7791F}
    .kpi-blue .kpi-value{color:#0C447C}
    .finding{background:#F0FBF6;border-left:3px solid #27AE60;border-radius:0 8px 8px 0;padding:11px 15px;font-size:13px;color:#1A5C35;margin:10px 0;line-height:1.6}
    .alert{background:#FDF2F2;border-left:3px solid #C0392B;border-radius:0 8px 8px 0;padding:11px 15px;font-size:13px;color:#7B1818;margin:10px 0;line-height:1.6}
    .warning{background:#FEF9EC;border-left:3px solid #F39C12;border-radius:0 8px 8px 0;padding:11px 15px;font-size:13px;color:#7D5A00;margin:10px 0;line-height:1.6}
    .critical{background:#FDF2F2;border-left:4px solid #7B1818;border-radius:0 8px 8px 0;padding:11px 15px;font-size:13px;color:#7B1818;margin:10px 0;line-height:1.6;font-weight:500}
    .section-title{font-size:15px;font-weight:600;color:#111;margin:18px 0 10px 0;padding-bottom:6px;border-bottom:1.5px solid #EBEBEB}
    .checker-result{background:white;border-radius:12px;padding:16px 20px;border:1px solid #E8E8E8;margin:8px 0}
    .checker-pass{border-left:4px solid #0A7540}
    .checker-fail{border-left:4px solid #C0392B}
    .checker-warn{border-left:4px solid #F39C12}
    footer{visibility:hidden}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load():
    base = Path(__file__).parent
    reqs    = pd.read_csv(base / "regulatory-requirements.csv")
    gaps    = pd.read_csv(base / "compliance-gaps.csv")
    risks   = pd.read_csv(base / "risk-register.csv")
    changes = pd.read_csv(base / "regulatory-change-log.csv")
    ops     = pd.read_csv(base / "operator-profiles.csv")
    with open(base / "key-findings.json") as f:
        findings = json.load(f)
    return reqs, gaps, risks, changes, ops, findings

reqs, gaps, risks, changes, ops, findings = load()

RISK_COLORS = {"Critical":"#7B1818","High":"#C0392B","Medium":"#B7791F","Low":"#0A7540"}

st.markdown("## Transport Canada Drone Compliance Analysis")
st.markdown("**Canadian Aviation Regulations Part IX** &nbsp;|&nbsp; 15 requirements mapped &nbsp;|&nbsp; 3 operator profiles assessed &nbsp;|&nbsp; 9 compliance gaps identified")
st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "  Compliance Overview  ",
    "  Operator Profiles  ",
    "  Risk Register  ",
    "  Regulatory Changes  ",
    "  Compliance Checker  ",
])

# ── TAB 1: OVERVIEW ───────────────────────────────────────────────────────────
with tab1:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""<div class="kpi kpi-blue">
            <div class="kpi-label">Requirements mapped</div>
            <div class="kpi-value">{findings['total_requirements']}</div>
            <div class="kpi-note">Transport Canada CAR Part IX rules</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class="kpi kpi-red">
            <div class="kpi-label">Compliance gaps found</div>
            <div class="kpi-value">{findings['total_compliance_gaps']}</div>
            <div class="kpi-note">{findings['immediate_gaps']} require immediate action</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<div class="kpi kpi-red">
            <div class="kpi-label">Critical risks identified</div>
            <div class="kpi-value">{findings['critical_risks']}</div>
            <div class="kpi-note">Including potential criminal liability</div>
        </div>""", unsafe_allow_html=True)
    with col4:
        st.markdown(f"""<div class="kpi kpi-amber">
            <div class="kpi-label">Max combined penalty</div>
            <div class="kpi-value">${findings['max_combined_penalty']:,}</div>
            <div class="kpi-note">Across all identified gaps</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("")
    st.markdown('<div class="critical">Most serious gap: The drone delivery operator (OP-003) is conducting Beyond Visual Line of Sight operations without a Special Flight Operations Certificate. This is illegal under CAR 901.70, carries a penalty of up to $25,000, and creates criminal liability in the event of any incident during delivery operations.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-title">Compliance gaps by urgency</div>', unsafe_allow_html=True)
        urgency_counts = gaps["Urgency"].value_counts().reset_index()
        urgency_counts.columns = ["Urgency", "Count"]
        urgency_order = ["Critical", "Immediate", "High", "Medium", "Low"]
        urgency_counts["Urgency"] = pd.Categorical(urgency_counts["Urgency"], categories=urgency_order, ordered=True)
        urgency_counts = urgency_counts.sort_values("Urgency")
        urgency_colors = {"Critical":"#7B1818","Immediate":"#C0392B","High":"#F59E0B","Medium":"#4285F4","Low":"#27AE60"}
        fig_urgency = px.bar(
            urgency_counts, x="Urgency", y="Count",
            color="Urgency",
            color_discrete_map=urgency_colors,
            text="Count",
        )
        fig_urgency.update_traces(textposition="outside")
        fig_urgency.update_layout(
            height=300, plot_bgcolor="white",
            yaxis=dict(title="Number of gaps", gridcolor="#F1F1F1"),
            xaxis=dict(title=""),
            showlegend=False,
            margin=dict(t=10, b=20),
        )
        st.plotly_chart(fig_urgency, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Risk ratings across all operators</div>', unsafe_allow_html=True)
        risk_counts = risks["Risk Rating"].value_counts().reset_index()
        risk_counts.columns = ["Rating", "Count"]
        fig_risk = px.pie(
            risk_counts, values="Count", names="Rating",
            color="Rating",
            color_discrete_map=RISK_COLORS,
            hole=0.45,
        )
        fig_risk.update_layout(height=300, margin=dict(t=10, b=20))
        st.plotly_chart(fig_risk, use_container_width=True)

    st.markdown('<div class="section-title">Requirements by category</div>', unsafe_allow_html=True)
    cat_counts = reqs["Category"].value_counts().reset_index()
    cat_counts.columns = ["Category", "Count"]
    fig_cat = px.bar(
        cat_counts.sort_values("Count"), x="Count", y="Category",
        orientation="h",
        color="Count",
        color_continuous_scale=["#94A3B8","#0C447C"],
        text="Count",
    )
    fig_cat.update_traces(textposition="outside")
    fig_cat.update_layout(
        height=320, plot_bgcolor="white",
        xaxis=dict(title="Number of requirements", gridcolor="#F1F1F1"),
        yaxis=dict(title=""),
        coloraxis_showscale=False,
        margin=dict(t=10, b=20),
    )
    st.plotly_chart(fig_cat, use_container_width=True)

# ── TAB 2: OPERATOR PROFILES ──────────────────────────────────────────────────
with tab2:
    st.markdown('<div class="section-title">Three operator profiles assessed against Transport Canada requirements</div>', unsafe_allow_html=True)

    profile_select = st.selectbox(
        "Select operator profile",
        ops["Profile Name"].tolist(),
        key="profile_select"
    )

    selected_profile = ops[ops["Profile Name"] == profile_select].iloc[0]
    profile_id = selected_profile["Profile ID"]
    profile_gaps = gaps[gaps["Profile ID"] == profile_id]
    profile_risks = risks[risks["Profile Name"] == profile_select]

    col1, col2, col3 = st.columns(3)
    with col1:
        total_gaps_profile = len(profile_gaps)
        compliant = len(profile_gaps[profile_gaps["Compliant"] == "Yes"])
        non_compliant = len(profile_gaps[profile_gaps["Compliant"] == "No"])
        card_class = "kpi-red" if non_compliant > 0 else "kpi-green"
        st.markdown(f"""<div class="kpi {card_class}">
            <div class="kpi-label">Compliance gaps</div>
            <div class="kpi-value">{total_gaps_profile}</div>
            <div class="kpi-note">{non_compliant} non-compliant, {compliant} partial</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        crit = len(profile_risks[profile_risks["Risk Rating"] == "Critical"])
        high = len(profile_risks[profile_risks["Risk Rating"] == "High"])
        st.markdown(f"""<div class="kpi kpi-red">
            <div class="kpi-label">Critical and high risks</div>
            <div class="kpi-value">{crit + high}</div>
            <div class="kpi-note">{crit} critical, {high} high</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        cert = selected_profile["Certification Status"]
        cert_class = "kpi-green" if "Advanced" in cert else "kpi-amber" if "Basic" in cert else "kpi-red"
        st.markdown(f"""<div class="kpi {cert_class}">
            <div class="kpi-label">Certification status</div>
            <div class="kpi-value" style="font-size:16px">{cert}</div>
            <div class="kpi-note">{selected_profile['Operator Type']} operator</div>
        </div>""", unsafe_allow_html=True)

    st.markdown(f'<div class="warning"><strong>Profile:</strong> {selected_profile["Description"]}</div>', unsafe_allow_html=True)

    if len(profile_gaps) > 0:
        st.markdown('<div class="section-title">Compliance gaps for this operator</div>', unsafe_allow_html=True)
        for _, gap in profile_gaps.iterrows():
            box_class = "alert" if gap["Compliant"] == "No" else "warning"
            st.markdown(f"""<div class="{box_class}">
                <strong>{gap['Gap ID']} — {gap['Requirement Summary']}</strong> ({gap['Urgency']})<br>
                {gap['Gap Description']}<br><br>
                <strong>Remediation:</strong> {gap['Remediation']}
            </div>""", unsafe_allow_html=True)
    else:
        st.markdown('<div class="finding">No compliance gaps identified for this operator profile.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Full operator profile details</div>', unsafe_allow_html=True)
    profile_display = pd.DataFrame(selected_profile).reset_index()
    profile_display.columns = ["Field", "Value"]
    st.dataframe(profile_display, use_container_width=True, hide_index=True)

# ── TAB 3: RISK REGISTER ──────────────────────────────────────────────────────
with tab3:
    st.markdown('<div class="section-title">Full risk register across all operator profiles</div>', unsafe_allow_html=True)
    st.markdown('<div class="alert">Risk rating is calculated as Likelihood multiplied by Consequence on a 1 to 4 scale each. Scores of 9 or above are Critical. 6 to 8 are High. 3 to 5 are Medium. Below 3 are Low.</div>', unsafe_allow_html=True)

    risk_filter = st.multiselect(
        "Filter by risk rating",
        ["Critical","High","Medium","Low"],
        default=["Critical","High","Medium","Low"],
        key="risk_filter"
    )

    filtered_risks = risks[risks["Risk Rating"].isin(risk_filter)]

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-title">Risk rating distribution</div>', unsafe_allow_html=True)
        fig_rr = go.Figure(go.Bar(
            x=["Critical","High","Medium","Low"],
            y=[
                len(risks[risks["Risk Rating"]=="Critical"]),
                len(risks[risks["Risk Rating"]=="High"]),
                len(risks[risks["Risk Rating"]=="Medium"]),
                len(risks[risks["Risk Rating"]=="Low"]),
            ],
            marker_color=["#7B1818","#C0392B","#B7791F","#0A7540"],
            text=[
                len(risks[risks["Risk Rating"]=="Critical"]),
                len(risks[risks["Risk Rating"]=="High"]),
                len(risks[risks["Risk Rating"]=="Medium"]),
                len(risks[risks["Risk Rating"]=="Low"]),
            ],
            textposition="outside",
        ))
        fig_rr.update_layout(
            height=260, plot_bgcolor="white",
            yaxis=dict(title="Number of risks", gridcolor="#F1F1F1"),
            xaxis=dict(title="Risk Rating"),
            margin=dict(t=10, b=20),
        )
        st.plotly_chart(fig_rr, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Maximum penalty by risk</div>', unsafe_allow_html=True)
        penalty_data = filtered_risks.copy()
        penalty_data["Penalty Numeric"] = penalty_data["Max Penalty"].str.extract(r'\$(\d{1,3}(?:,\d{3})*)').replace(',', '', regex=True).astype(float, errors='ignore')
        fig_pen = px.bar(
            filtered_risks,
            x="Risk ID", y=filtered_risks["Max Penalty"].str.extract(r'(\d+[\d,]*)')[0].str.replace(',','').astype(float, errors='coerce').fillna(0),
            color="Risk Rating",
            color_discrete_map=RISK_COLORS,
            text="Max Penalty",
        )
        fig_pen.update_traces(textposition="outside", textfont_size=9)
        fig_pen.update_layout(
            height=260, plot_bgcolor="white",
            yaxis=dict(title="Max Penalty (CAD)", gridcolor="#F1F1F1", tickformat="$,.0f"),
            xaxis=dict(title=""),
            margin=dict(t=10, b=20),
        )
        st.plotly_chart(fig_pen, use_container_width=True)

    st.markdown('<div class="section-title">Detailed risk register</div>', unsafe_allow_html=True)
    display_cols = ["Risk ID","Profile Name","Risk Description","Likelihood","Consequence","Risk Rating","Max Penalty","Recommended Action"]
    st.dataframe(filtered_risks[display_cols], use_container_width=True, hide_index=True)

# ── TAB 4: REGULATORY CHANGES ─────────────────────────────────────────────────
with tab4:
    st.markdown('<div class="section-title">Transport Canada drone regulatory changes since 2019</div>', unsafe_allow_html=True)
    st.markdown('<div class="finding">Transport Canada has been actively evolving its drone regulatory framework since the foundational 2019 rules came into force. The most important recent development is increased enforcement activity in 2024, which means compliance gaps that previously carried low practical risk are now being actively pursued.</div>', unsafe_allow_html=True)

    for _, change in changes.iterrows():
        box_class = "alert" if "criminal" in change["Compliance Implication"].lower() or "Immediate" in change["Urgency for Existing Operators"] else "warning" if "Important" in change["Urgency for Existing Operators"] else "finding"
        st.markdown(f"""<div class="{box_class}">
            <strong>{change['Change ID']} — {change['Effective Date']}</strong><br>
            <strong>{change['Change Summary']}</strong><br><br>
            {change['What Changed']}<br><br>
            <strong>Who is affected:</strong> {change['Who Is Affected']}<br>
            <strong>Compliance implication:</strong> {change['Compliance Implication']}
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-title">Full regulatory change log</div>', unsafe_allow_html=True)
    st.dataframe(changes, use_container_width=True, hide_index=True)

# ── TAB 5: COMPLIANCE CHECKER ─────────────────────────────────────────────────
with tab5:
    st.markdown('<div class="section-title">Transport Canada Drone Compliance Checker</div>', unsafe_allow_html=True)
    st.markdown("Answer the questions below and get an instant plain English assessment of which Transport Canada rules apply to you and whether you meet them.")
    st.markdown("")

    col1, col2 = st.columns(2)
    with col1:
        drone_weight = st.selectbox("What is your drone's weight?", ["Under 250g (minimal rules apply)", "250g to 1kg", "1kg to 25kg", "Over 25kg"])
        operator_type = st.selectbox("How do you use your drone?", ["Recreation and hobby", "Commercial work (paid or for business)"])
        certification = st.selectbox("What certification do you hold?", ["None", "Basic Operations certificate", "Advanced Operations certificate"])

    with col2:
        registration = st.selectbox("Is your drone registered with Transport Canada?", ["Yes", "No", "Not sure"])
        location_type = st.selectbox("Where do you typically fly?", ["Open rural areas far from airports", "Parks and suburban areas", "Near an airport or in controlled airspace", "Near people or crowds", "Beyond visual line of sight"])
        night_ops = st.selectbox("Do you fly at night?", ["No", "Yes with anti-collision lighting", "Yes without proper lighting"])

    st.markdown("")
    if st.button("Check my compliance", type="primary"):
        results = []

        if "250g" in drone_weight or "1kg" in drone_weight or "25kg" in drone_weight:
            if registration == "No" or registration == "Not sure":
                results.append({"status":"fail","rule":"REG-001 — Registration","message":"Your drone requires Transport Canada registration. Register at tc.canada.ca for $5. Takes 15 minutes.","urgency":"Immediate"})
            else:
                results.append({"status":"pass","rule":"REG-001 — Registration","message":"Your drone is registered. Good.","urgency":"None"})

            if certification == "None":
                results.append({"status":"fail","rule":"REG-002 or REG-003 — Pilot certificate","message":"You need at least a Basic Operations certificate before flying. Study for and pass the free online exam at tc.canada.ca.","urgency":"Immediate"})
            elif certification == "Basic Operations certificate" and operator_type == "Commercial work (paid or for business)" and location_type == "Near people or crowds":
                results.append({"status":"fail","rule":"REG-003 — Advanced certificate required","message":"Commercial operations near people require an Advanced certificate, not just Basic. You need to pass the Advanced exam and complete a flight review.","urgency":"Immediate"})
            else:
                results.append({"status":"pass","rule":"REG-002 or REG-003 — Pilot certificate","message":f"You hold a {certification}. This covers your stated use case.","urgency":"None"})

        if location_type == "Near an airport or in controlled airspace":
            results.append({"status":"warn","rule":"REG-006 — Controlled airspace authorization","message":"You must obtain authorization through the NAV CANADA NAS app before every flight in controlled airspace. Download it and check before you fly.","urgency":"High"})

        if location_type == "Beyond visual line of sight":
            results.append({"status":"fail","rule":"REG-012 — Special Flight Operations Certificate required","message":"Beyond visual line of sight operations are illegal without a Special Flight Operations Certificate from Transport Canada. Apply before conducting any BVLOS operations.","urgency":"Critical"})

        if night_ops == "Yes without proper lighting":
            results.append({"status":"fail","rule":"REG-013 — Night operations lighting","message":"Night operations require anti-collision lighting visible from at least 1km in all directions. Stop night flying until compliant lighting is installed.","urgency":"High"})
        elif night_ops == "Yes with anti-collision lighting":
            results.append({"status":"pass","rule":"REG-013 — Night operations lighting","message":"You have the required lighting for night operations.","urgency":"None"})

        if "Under 250g" in drone_weight:
            results.append({"status":"pass","rule":"All weight-based requirements","message":"Your drone is under 250g. Most Transport Canada RPAS rules do not apply. You still cannot fly in restricted airspace or endanger anyone.","urgency":"None"})

        st.markdown('<div class="section-title">Your compliance assessment</div>', unsafe_allow_html=True)
        critical_count = sum(1 for r in results if r["status"] == "fail" and r["urgency"] == "Critical")
        fail_count = sum(1 for r in results if r["status"] == "fail")
        pass_count = sum(1 for r in results if r["status"] == "pass")

        if fail_count == 0:
            st.markdown('<div class="finding"><strong>Overall: Compliant</strong> — Based on your inputs you appear to meet the applicable Transport Canada requirements. Always check the NAS app before flying in unfamiliar locations.</div>', unsafe_allow_html=True)
        elif critical_count > 0:
            st.markdown(f'<div class="critical"><strong>Overall: Critical gaps found</strong> — {fail_count} compliance {"gap" if fail_count == 1 else "gaps"} identified. {critical_count} {"is" if critical_count == 1 else "are"} critical and must be resolved before your next flight.</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="alert"><strong>Overall: Gaps found</strong> — {fail_count} compliance {"gap" if fail_count == 1 else "gaps"} identified. Review the items below and resolve before your next flight.</div>', unsafe_allow_html=True)

        for r in results:
            if r["status"] == "fail":
                box_class = "critical" if r["urgency"] == "Critical" else "alert"
            elif r["status"] == "warn":
                box_class = "warning"
            else:
                box_class = "finding"
            urgency_text = f" — {r['urgency']}" if r["urgency"] != "None" else ""
            st.markdown(f"""<div class="{box_class}">
                <strong>{r['rule']}{urgency_text}</strong><br>{r['message']}
            </div>""", unsafe_allow_html=True)

st.divider()
st.markdown(
    "**Regulatory note:** This tool is for educational and portfolio purposes. "
    "All regulatory references are based on Transport Canada Canadian Aviation Regulations Part IX as published at tc.canada.ca. "
    "Rules change regularly. Always verify current requirements directly with Transport Canada before any flight operation. "
    "Prepared by Simran Saran as part of The Case Files portfolio series."
)
