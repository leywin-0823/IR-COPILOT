from app.attack.techniques import AttackTechnique

ATTACK_TECHNIQUES = {
    "T1110": AttackTechnique(
        technique_id="T1110",
        name="Brute Force",
        tactics=["credential_access"],
        description="Adversaries attempt to gain access by guessing credentials.",
        detection_notes="Multiple failed authentication attempts across one or more accounts."
    ),
    "T1078": AttackTechnique(
        technique_id="T1078",
        name="Valid Accounts",
        tactics=["initial_access", "persistence"],
        description="Adversaries use valid credentials to gain access.",
        detection_notes="Successful login using privileged or unusual accounts."
    )
}
