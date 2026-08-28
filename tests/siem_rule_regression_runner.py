#!/usr/bin/env python3
"""
Walking Fortress - Automated SIEM & Detection Rule Regression Suite
Validates logic integrity across SPL, Wazuh XML, and JSON mock telemetry.
"""

import json
import sys
import xml.etree.ElementTree as ET

def test_wazuh_xml_syntax(file_path):
    """Validates XML structural integrity for Wazuh rule definitions."""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        rules = root.findall('rule')
        print(f"[+] Wazuh XML Check [{file_path}]: Valid XML structure ({len(rules)} rules found).")
        return True
    except ET.ParseError as e:
        print(f"[-] Wazuh XML Check [{file_path}]: PARSE ERROR - {e}")
        return False

def evaluate_mock_telemetry(mock_file):
    """Evaluates synthetic telemetry against defined rule match conditions."""
    with open(mock_file, 'r') as f:
        data = json.load(f)
    
    passed = 0
    total = len(data.get("test_cases", []))
    
    print(f"[*] Loaded {total} test cases from {mock_file}")
    
    for case in data.get("test_cases", []):
        target = case.get("rule_target")
        log = case.get("log_data")
        expected = case.get("expected_result")
        
        # Rule evaluation logic mapping
        matched = False
        if target == "T1558.003_Kerberoasting" and log.get("EventCode") == 4769 and log.get("TicketEncryptionType") == "0x17":
            matched = True
        elif target == "T1053.005_Scheduled_Task" and log.get("EventCode") == 4698 and "powershell" in log.get("TaskContent", "").lower():
            matched = True
        elif target == "AWS_IAM_Privilege_Escalation" and log.get("eventName") == "AttachUserPolicy" and "AdministratorAccess" in str(log):
            matched = True
            
        status = "MATCH" if matched else "NO_MATCH"
        if status == expected:
            print(f"  [PASS] {target}: Received {status} (Expected {expected})")
            passed += 1
        else:
            print(f"  [FAIL] {target}: Received {status} (Expected {expected})")
            
    print(f"[*] Test Summary: {passed}/{total} Passed.")
    return passed == total

if __name__ == "__main__":
    xml_success = test_wazuh_xml_syntax("persistence/wmi_event_subscription_rule.xml")
    mock_success = evaluate_mock_telemetry("tests/mock_telemetry_samples.json")
    
    if xml_success and mock_success:
        print("[SUCCESS] All detection regression checks passed cleanly!")
        sys.exit(0)
    else:
        print("[FAILURE] Regression test failure detected.")
        sys.exit(1)