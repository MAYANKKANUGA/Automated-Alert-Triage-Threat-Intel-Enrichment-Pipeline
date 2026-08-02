### 🚨 Automated SOC Incident Report

**Rule Description:** $exec.title
**Rule ID:** $exec.rule_id
**Timestamp:** $exec.timestamp

---

### 🌐 IOC Details (Attacker IP)
* **IP Address:** `$ioc.message.ioc.value`
* **City:** $geoip_lookup_1.message.city
* **Country:** $geoip_lookup_1.message.country
* **ASN:** $geoip_lookup_1.message.asn

---

### 🛡️ Threat Intelligence Scoring
* **VirusTotal Malicious Hits:** $enrichment_aggregator.message.aggregated_report.threat_scores.virustotal_malicious_hits
* **AbuseIPDB Confidence Score:** $enrichment_aggregator.message.aggregated_report.threat_scores.abuseipdb_confidence_score%

---

### 📊 Risk Assessment
* **SOC Risk Score:** $risk_scoring.message.risk_score / 120
* **Severity:** $risk_scoring.message.severity_name
* **Action Recommended:** $risk_scoring.message.recommended_action

---

### 💻 Targeted Endpoint
* **Agent Name:** $exec.all_fields.agent.name
* **Target IP:** $exec.all_fields.agent.ip
* **User:** $exec.all_fields.data.srcuser