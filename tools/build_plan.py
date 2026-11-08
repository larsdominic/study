# Writes tools/plan.json and tools/links.json from tools/plan_data.py (run before landing.py).
# The same plan_data.py fills the study sheet's Daily plan tab (Drive links in columns K to Y, site link in Z).
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plan_data import DAYS
here = os.path.dirname(os.path.abspath(__file__))
json.dump([dict(iso=d['iso'], date=d['date'], day=d['day'], week=d['week'], subject=d['subject'], task=d['task']) for d in DAYS],
          open(os.path.join(here, 'plan.json'), 'w'), indent=0, ensure_ascii=False)
json.dump({d['iso']: d['guide'] for d in DAYS if d['guide']}, open(os.path.join(here, 'links.json'), 'w'), indent=1, ensure_ascii=False)
print('plan', len(DAYS), 'days')
