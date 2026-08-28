## Custom Zeek Script to detect oversized DNS queries (Potential Tunneling/C2)
module WalkingFortress;

export {
    redef enum Notice::Type += {
        Suspicious_Large_DNS_Query
    };
}

event dns_request(c: connection, msg: dns_msg, query: string)
    {
    # Trigger a Notice log if a DNS query exceeds 60 characters
    if ( |query| > 60 )
        {
        NOTICE([$note=Suspicious_Large_DNS_Query,
                $msg=fmt("Possible DNS Tunneling attempt detected: %s", query),
                $conn=c,
                $identifier=cat(c$id$orig_h, query)]);
        }
    }