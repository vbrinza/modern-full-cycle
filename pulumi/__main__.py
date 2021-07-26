"""Deployer"""
import pulumi
from pulumi_kubernetes.helm.v3 import Chart, ChartOpts, FetchOpts
from pulumi_kubernetes.core.v1 import Namespace

crt_mgr_name_space = Namespace("cert-manager",
                               metadata={}
                               )
demo_app_name_space = Namespace("demo-web-app",
                                metadata={}
                                )
monitoring_name_space = Namespace("monitoring",
                                  metadata={}
                                  )
pulumi.export('crt_mgr_name_space', crt_mgr_name_space.metadata.apply(lambda m: m.name))
pulumi.export('demo_app_name_space', demo_app_name_space.metadata.apply(lambda m: m.name))
pulumi.export('monitoring_name_space', monitoring_name_space.metadata.apply(lambda m: m.name))

nginx_ingress = Chart(
    "cert-manager",
    ChartOpts(
        chart="cert-manager",
        namespace=crt_mgr_name_space.id,
        version="v1.4.0",
        fetch_opts=FetchOpts(
            repo="https://charts.jetstack.io//",
        )
    )
)

prometheus = Chart(
    "prometheus",
    ChartOpts(
        chart="prometheus",
        namespace=monitoring_name_space.id,
        fetch_opts=FetchOpts(
            repo="https://prometheus-community.github.io/helm-charts//",
        )
    )
)

grafana = Chart(
    "grafana",
    ChartOpts(
        chart="grafana",
        namespace=monitoring_name_space.id,
        fetch_opts=FetchOpts(
            repo="https://grafana.github.io/helm-charts//",
        )
    )
)

app = Chart(
    "demo-web-app",
    ChartOpts(
        chart="juice-shop",
        namespace=demo_app_name_space.id,
        version="2.9.1",
        fetch_opts=FetchOpts(
            repo="https://charts.securecodebox.io//",
        ),
        values={
            "replicaCount": 3
        }
    )
)
