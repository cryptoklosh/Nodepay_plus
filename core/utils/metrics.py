from prometheus_client import Gauge, Info, Counter

nodepay_info = Info("nodepay", "Info about nodepay node")
mined_nodepay_gauge = Gauge('mined_nodepay', 'Number of mined nodepay points', ['account'])
nodepay_requests_total_counter = Counter('nodepay_requests_total', 'API requests', ['account', 'status'])