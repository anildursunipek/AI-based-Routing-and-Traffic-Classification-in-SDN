import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TopologyService {

  constructor(private http:HttpClient) { }

  topologyStart(){
    return this.http.get<any>("http://127.0.0.1:5000/topology/start");
  }

  topologyStop(){
    return this.http.get<any>("http://127.0.0.1:5000/topology/stop");
  }

  getHostsCount(){
    return this.http.get<any>("http://127.0.0.1:5000/topology/get-host-count");
  }

  getSwitchsCount(){
    return this.http.get<any>("http://127.0.0.1:5000/topology/get-switch-count");
  }

  getLinksCount(){
    return this.http.get<any>("http://127.0.0.1:5000/topology/get-link-count");
  }

  getSystemStatus(){
    return this.http.get<any>("http://127.0.0.1:5000/topology/get-system-status");
  }

  getStartDate(){
    return this.http.get<any>("http://127.0.0.1:5000/topology/get-start-date");
  }

  getHosts(){
    return this.http.get<any>("http://127.0.0.1:5000/get-hosts");
  }

  getSwitches(){
    return this.http.get<any>("http://127.0.0.1:5000/get-switchs");
  }

  generateTraffic(){
    return this.http.get<any>("http://127.0.0.1:5000/topology/generate/traffic");
  }

  getTraffic(){
    return this.http.get<any>("http://127.0.0.1:5000/topology/get/traffic");
  }
}
