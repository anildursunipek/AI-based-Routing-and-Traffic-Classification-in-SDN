export class Host{
    name:string;
    MAC:string;
    IP:string;
}

export class Switch{
    name:string;
    dpid:string;
    ports:string;
    host_connections:Host[] = new Array();
}