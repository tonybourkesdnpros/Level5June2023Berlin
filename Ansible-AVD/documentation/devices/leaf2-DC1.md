# leaf2-DC1
# Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [DNS Domain](#dns-domain)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
- [Monitoring](#monitoring)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router OSPF](#router-ospf)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
- [ACL](#acl)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Quality Of Service](#quality-of-service)

# Management

## Management Interfaces

### Management Interfaces Summary

#### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | oob_management | oob | default | 192.168.0.22/24 | 192.168.0.1 |

#### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | oob_management | oob | default | -  | - |

### Management Interfaces Device Configuration

```eos
!
interface Management0
   description oob_management
   no shutdown
   ip address 192.168.0.22/24
```

## DNS Domain

### DNS domain: atd.lab

### DNS Domain Device Configuration

```eos
dns domain atd.lab
!
```

## Management API HTTP

### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| default | - | - |

### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf default
      no shutdown
```

# Authentication

# Monitoring

# MLAG

## MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| mlag1-DC1 | Vlan4094 | 10.255.252.0 | Port-Channel1 |

Dual primary detection is disabled.

## MLAG Device Configuration

```eos
!
mlag configuration
   domain-id mlag1-DC1
   local-interface Vlan4094
   peer-address 10.255.252.0
   peer-link Port-Channel1
   reload-delay mlag 300
   reload-delay non-mlag 330
```

# Spanning Tree

## Spanning Tree Summary

STP mode: **mstp**

### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 16384 |

### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4093-4094**

## Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
no spanning-tree vlan-id 4093-4094
spanning-tree mst 0 priority 16384
```

# Internal VLAN Allocation Policy

## Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

## Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

# VLANs

## VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 10 | DMZ | - |
| 20 | Internal | - |
| 3999 | MLAG_iBGP_Spock | LEAF_PEER_L3 |
| 4093 | LEAF_PEER_L3 | LEAF_PEER_L3 |
| 4094 | MLAG_PEER | MLAG |

## VLANs Device Configuration

```eos
!
vlan 10
   name DMZ
!
vlan 20
   name Internal
!
vlan 3999
   name MLAG_iBGP_Spock
   trunk group LEAF_PEER_L3
!
vlan 4093
   name LEAF_PEER_L3
   trunk group LEAF_PEER_L3
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
```

# Interfaces

## Ethernet Interfaces

### Ethernet Interfaces Summary

#### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | MLAG_PEER_leaf1-DC1_Ethernet1 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 1 |
| Ethernet2 | MLAG_PEER_leaf1-DC1_Ethernet2 | *trunk | *2-4094 | *- | *['LEAF_PEER_L3', 'MLAG'] | 1 |
| Ethernet6 | host1-DC1_E3 | *access | *10 | *- | *- | 6 |
| Ethernet7 | host1-DC1_E4 | *access | *10 | *- | *- | 6 |

*Inherited from Port-Channel Interface

#### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet3 | P2P_LINK_TO_SPINE1-DC1_Ethernet3 | routed | - | 192.168.103.7/31 | default | 9000 | False | - | - |
| Ethernet4 | P2P_LINK_TO_SPINE2-DC1_Ethernet3 | routed | - | 192.168.103.9/31 | default | 9000 | False | - | - |
| Ethernet5 | P2P_LINK_TO_SPINE3-DC1_Ethernet3 | routed | - | 192.168.103.11/31 | default | 9000 | False | - | - |

### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description MLAG_PEER_leaf1-DC1_Ethernet1
   no shutdown
   channel-group 1 mode active
!
interface Ethernet2
   description MLAG_PEER_leaf1-DC1_Ethernet2
   no shutdown
   channel-group 1 mode active
!
interface Ethernet3
   description P2P_LINK_TO_SPINE1-DC1_Ethernet3
   no shutdown
   mtu 9000
   no switchport
   ip address 192.168.103.7/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet4
   description P2P_LINK_TO_SPINE2-DC1_Ethernet3
   no shutdown
   mtu 9000
   no switchport
   ip address 192.168.103.9/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet5
   description P2P_LINK_TO_SPINE3-DC1_Ethernet3
   no shutdown
   mtu 9000
   no switchport
   ip address 192.168.103.11/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Ethernet6
   description host1-DC1_E3
   no shutdown
   channel-group 6 mode active
!
interface Ethernet7
   description host1-DC1_E4
   no shutdown
   channel-group 6 mode active
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

#### L2

| Interface | Description | Type | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | MLAG_PEER_leaf1-DC1_Po1 | switched | trunk | 2-4094 | - | ['LEAF_PEER_L3', 'MLAG'] | - | - | - | - |
| Port-Channel6 | host1-DC1_host`-DC1 | switched | access | 10 | - | - | - | - | 6 | - |

### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description MLAG_PEER_leaf1-DC1_Po1
   no shutdown
   switchport
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
!
interface Port-Channel6
   description host1-DC1_host`-DC1
   no shutdown
   switchport
   switchport access vlan 10
   mlag 6
   spanning-tree portfast
```

## Loopback Interfaces

### Loopback Interfaces Summary

#### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.101.2/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.102.1/32 |

#### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |


### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 192.168.101.2/32
   ip ospf area 0.0.0.0
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ip address 192.168.102.1/32
   ip ospf area 0.0.0.0
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan10 | DMZ | Spock | - | False |
| Vlan20 | Internal | Spock | - | False |
| Vlan3999 | MLAG_PEER_L3_iBGP: vrf Spock | Spock | 9000 | False |
| Vlan4093 | MLAG_PEER_L3_PEERING | default | 9000 | False |
| Vlan4094 | MLAG_PEER | default | 9000 | False |

#### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |
| Vlan10 |  Spock  |  -  |  10.1.10.1/24  |  -  |  -  |  -  |  -  |
| Vlan20 |  Spock  |  -  |  10.1.20.1/24  |  -  |  -  |  -  |  -  |
| Vlan3999 |  Spock  |  10.255.251.1/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4093 |  default  |  10.255.251.1/31  |  -  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  10.255.252.1/31  |  -  |  -  |  -  |  -  |  -  |

### VLAN Interfaces Device Configuration

```eos
!
interface Vlan10
   description DMZ
   no shutdown
   vrf Spock
   ip address virtual 10.1.10.1/24
!
interface Vlan20
   description Internal
   no shutdown
   vrf Spock
   ip address virtual 10.1.20.1/24
!
interface Vlan3999
   description MLAG_PEER_L3_iBGP: vrf Spock
   no shutdown
   mtu 9000
   vrf Spock
   ip address 10.255.251.1/31
!
interface Vlan4093
   description MLAG_PEER_L3_PEERING
   no shutdown
   mtu 9000
   ip address 10.255.251.1/31
   ip ospf network point-to-point
   ip ospf area 0.0.0.0
!
interface Vlan4094
   description MLAG_PEER
   no shutdown
   mtu 9000
   no autostate
   ip address 10.255.252.1/31
```

## VXLAN Interface

### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |
| EVPN MLAG Shared Router MAC | mlag-system-id |

#### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 10 | 20 | - | - |
| 20 | 30 | - | - |

#### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Spock | 1000 | - |

### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description leaf2-DC1_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 10 vni 20
   vxlan vlan 20 vni 30
   vxlan vrf Spock vni 1000
```

# Routing
## Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

## Virtual Router MAC Address

### Virtual Router MAC Address Summary

#### Virtual Router MAC Address: 00:1c:73:00:00:99

### Virtual Router MAC Address Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:00:99
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| default | false |
| Spock | true |

### IP Routing Device Configuration

```eos
!
ip routing
ip routing vrf Spock
```
## IPv6 Routing

### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| default | false |
| Spock | false |

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| default | 0.0.0.0/0 | 192.168.0.1 | - | 1 | - | - | - |

### Static Routes Device Configuration

```eos
!
ip route 0.0.0.0/0 192.168.0.1
```

## Router OSPF

### Router OSPF Summary

| Process ID | Router ID | Default Passive Interface | No Passive Interface | BFD | Max LSA | Default Information Originate | Log Adjacency Changes Detail | Auto Cost Reference Bandwidth | Maximum Paths | MPLS LDP Sync Default | Distribute List In |
| ---------- | --------- | ------------------------- | -------------------- | --- | ------- | ----------------------------- | ---------------------------- | ----------------------------- | ------------- | --------------------- | ------------------ |
| 100 | 192.168.101.2 | enabled | Ethernet3 <br> Ethernet4 <br> Ethernet5 <br> Vlan4093 <br> | disabled | 12000 | disabled | disabled | - | - | - | - |

### OSPF Interfaces

| Interface | Area | Cost | Point To Point |
| -------- | -------- | -------- | -------- |
| Ethernet3 | 0.0.0.0 | - | True |
| Ethernet4 | 0.0.0.0 | - | True |
| Ethernet5 | 0.0.0.0 | - | True |
| Vlan4093 | 0.0.0.0 | - | True |
| Loopback0 | 0.0.0.0 | - | - |
| Loopback1 | 0.0.0.0 | - | - |

### Router OSPF Device Configuration

```eos
!
router ospf 100
   router-id 192.168.101.2
   passive-interface default
   no passive-interface Ethernet3
   no passive-interface Ethernet4
   no passive-interface Ethernet5
   no passive-interface Vlan4093
   max-lsa 12000
```

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101|  192.168.101.2 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 4 ecmp 4 |

### Router BGP Peer Groups

#### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- |
| 192.168.101.11 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.101.12 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 192.168.101.13 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - |
| 10.255.251.0 | - | Spock | - | - | - | - | - | - |

### Router BGP EVPN Address Family

#### EVPN Peer Groups

| Peer Group | Activate |
| ---------- | -------- |
| EVPN-OVERLAY-PEERS | True |

### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 10 | 192.168.101.2:20 | 20:20 | - | - | learned |
| 20 | 192.168.101.2:30 | 30:30 | - | - | learned |

### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Spock | 192.168.101.2:1000 | connected |

### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 192.168.101.2
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor 192.168.101.11 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.11 remote-as 65100
   neighbor 192.168.101.11 description spine1-DC1
   neighbor 192.168.101.12 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.12 remote-as 65100
   neighbor 192.168.101.12 description spine2-DC1
   neighbor 192.168.101.13 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.13 remote-as 65100
   neighbor 192.168.101.13 description spine3-DC1
   !
   vlan 10
      rd 192.168.101.2:20
      route-target both 20:20
      redistribute learned
   !
   vlan 20
      rd 192.168.101.2:30
      route-target both 30:30
      redistribute learned
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
   !
   vrf Spock
      rd 192.168.101.2:1000
      route-target import evpn 1000:1000
      route-target export evpn 1000:1000
      router-id 192.168.101.2
      neighbor 10.255.251.0 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
```

# BFD

## Router BFD

### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 300 min-rx 300 multiplier 3
```

# Multicast

## IP IGMP Snooping

### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

### IP IGMP Snooping Device Configuration

```eos
```

# Filters

# ACL

# VRF Instances

## VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| default | disabled |
| Spock | enabled |

## VRF Instances Device Configuration

```eos
!
vrf instance Spock
```

# Quality Of Service
