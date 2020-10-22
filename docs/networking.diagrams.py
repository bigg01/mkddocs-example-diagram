from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.logging import Fluentd
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx
from diagrams.onprem.queue import Kafka

from diagrams.k8s.compute import Pod, StatefulSet, Deploy
from diagrams.k8s.network import Service, NetworkPolicy, Ingress
from diagrams.k8s.storage import PV, PVC, StorageClass
from diagrams.k8s.ecosystem import Helm

from diagrams.generic.network import Router

from diagrams.generic.database import SQL

from diagrams.onprem.monitoring import Splunk

#(png, jpg, svg, and pdf) are allowed.
with Diagram(name="OCP3_Ingress_Egress", show=False, outformat="png"):


    #metrics = Prometheus("metric")
    #metrics << Edge(color="firebrick", style="dashed") << Grafana("monitoring")

    #helm = Helm("deploy1")
    #deploy1 = Deploy("deploy1")

    
  
    
    
    serverExtA = Server("DB Server")

    #serverExtB = Server("DB Server")

    with Cluster("Ingress Router ZONE A"):
        haproxy_ingressA = Ingress("app1.example.com")
    
    #with Cluster("Ingress Router ZONE B"):
    #    haproxy_ingressB = Ingress("haroxy")

    with Cluster("Egress Router Namespace A"):
        haproxy_egressA= Ingress("haproxy")
    
    #with Cluster("Egress Router Namespace B"):
    #    haproxy_egressB= Ingress("haproxy")

    with Cluster("Namespace A"):
        #POD1 = Pod("frontend")
        PODF = [Pod("frontend"),Pod("frontend"),Pod("frontend")]
        PODB = [Pod("backend"),Pod("backend"),Pod("backend")]
        haproxy_ingressA >> Edge(color="brown") >> Service("frontend") >> PODF >>  Service("backend") >> PODB >> SQL("Replica1") >> haproxy_egressA >> serverExtA
    
    with Cluster("Namespace Metrics"):
        metrics = Prometheus("metric")
        PODF >> metrics << Edge(color="firebrick", style="dashed") << Grafana("monitoring")
    with Cluster("Namespace Logging"):
        PODF >> Fluentd("forwarder") >> Splunk("CentralLogging")

    #with Cluster("Namespace B"):
    #    masterB = Pod("POD 3")
    #    masterB - Pod("POD 4")  >> haproxy_egressB >>  SQL("Replica1") >> serverExtB
    #    haproxy_ingressB >> Edge(color="black") >> masterB

    #aggregator = Fluentd("logging")
    #aggregator >> Edge(label="parse") >> Kafka("stream") >> Edge(color="black", style="bold") >> Spark("analytics")

   # haproxy_ingress  >> Edge(color="darkorange") 