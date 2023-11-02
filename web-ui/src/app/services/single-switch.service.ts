import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Switch } from '../model';

@Injectable({
  providedIn: 'root'
})
export class SingleSwitchService {

  constructor(private http:HttpClient) { }

  startSingleSwitchTopo(mySwitch: Switch){
    return this.http.post<any>("http://127.0.0.1:5000/start/single-switch-topo", mySwitch);
  }

  stopSingleSwitchTopo(){
    return this.http.get<any>("http://127.0.0.1:5000/stop/single-switch-topo");
  }

  getHostsCount(){
    return this.http.get<any>("http://127.0.0.1:5000/get-host-count");
  }

  getSwitchsCount(){
    return this.http.get<any>("http://127.0.0.1:5000/get-switch-count");
  }

  getLinksCount(){
    return this.http.get<any>("http://127.0.0.1:5000/get-link-count");
  }

  getSystemStatus(){
    return this.http.get<any>("http://127.0.0.1:5000/get-system-status");
  }

  getStartDate(){
    return this.http.get<any>("http://127.0.0.1:5000/get-start-date");
  }


  getHosts(){
    return this.http.get<any>("http://127.0.0.1:5000/get-hosts");
  }

  getSwitches(){
    return this.http.get<any>("http://127.0.0.1:5000/get-switchs");
  }
}
