import json

# FIX 1: Pointing to last_analysis_stats (Correct VT Hits)
vt_hits = """$virustotal_v3_1.body.data.attributes.last_analysis_stats.malicious"""      

# FIX 2: Corrected the typo in the variable path (Correct AbuseIPDB Score)
abuse_score_raw = """$abuseipdb.body.data.abuseConfidenceScore"""   

# Map to: $ioc.message.ioc.value
ip_raw = """$ioc.message.ioc.value"""      

try:
    # Safely convert scores to numbers
    try:
        vt_malicious = int(vt_hits.strip())
    except:
        vt_malicious = 0
        
    try:
        abuse_score = int(abuse_score_raw.strip())
    except:
        abuse_score = 0
        
    ip_value = ip_raw.strip() if ip_raw.strip() else "Unknown_IP"
    
    # SOC Decision Logic
    is_malicious = False
    if vt_malicious > 0 or abuse_score > 20:
        is_malicious = True
        
    summary = {
        "ioc": ip_value,
        "threat_scores": {
            "virustotal_malicious_hits": vt_malicious,
            "abuseipdb_confidence_score": abuse_score
        },
        "soc_analysis": {
            "is_malicious": is_malicious,
            "recommended_action": "BLOCK" if is_malicious else "ALLOW_AND_MONITOR"
        }
    }
    
    print(json.dumps({"success": True, "aggregated_report": summary}))
    
except Exception as e:
    print(json.dumps({"success": False, "error": str(e)}))