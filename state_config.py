"""
State configuration for this VirginIslandsDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "VI"
STATE_NAME = "U.S. Virgin Islands"
APP_NAME = "VirginIslandsDischargeWatch"
APP_TAGLINE = "U.S. Virgin Islands Discharge Monitoring"
DOMAIN = "virginislandsdischargewatch.org"
DATA_FILE = "vi_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@virginislandsdischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "AST"
EPA_REGION = 2
