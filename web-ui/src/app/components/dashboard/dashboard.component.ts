import { Component, OnInit } from '@angular/core';
import { Switch, Host } from 'src/app/model';
import { SingleSwitchService } from 'src/app/services/single-switch.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  value: string;

  switchInputCount: number;
  hostInputCount: number

  hostCount: number;
  switchCount: number;
  linkCount: number;

  switchDisable: boolean = false;
  hostDisable: boolean = false;
  systemStatus: boolean;

  topoStartDate: Date;
  upTime: string = "00:00:00";

  paymentOptions: any[] = [
    { name: 'Topology (Single)', value: "SINGLE_SWITCH_TOPO" },
  ];
  constructor(private singleSwitchService: SingleSwitchService) {

  }

  ngOnInit(): void {
    this.getSystemStatus();

  }

  selectButtonChanged() {
    if (this.value == "SINGLE_SWITCH_TOPO") {
      this.selectedSingleSwitchTopo();
    }
  }

  selectedSingleSwitchTopo() {
    this.switchInputCount = 1;
    this.hostInputCount = 1
    this.switchDisable = true;
    this.hostDisable = false;
  }

  createSwitchAndHost() {
    let mySwitch: Switch = new Switch();
    mySwitch.name = "s1"
    for (let j = 0; j < this.hostInputCount; j++) {
      let host: Host = new Host();
      host.name = "h" + (j + 1)
      mySwitch.host_connections.push(host);
    }
    return mySwitch;
  }

  startSingleSwitchTopo() {
    let mySwitch = this.createSwitchAndHost();

    this.singleSwitchService.startSingleSwitchTopo(mySwitch).subscribe(res => {
      console.log(res);
      this.getSystemStatus();
    }, err => {
      // err
    })
  }

  getHostCount() {
    this.singleSwitchService.getHostsCount().subscribe(res => {
      this.hostCount = res.result;
    })
  }

  getSwitchCount() {
    this.singleSwitchService.getSwitchsCount().subscribe(res => {
      this.switchCount = res.result;
    })
  }

  getLinksCount() {
    this.singleSwitchService.getLinksCount().subscribe(res => {
      this.linkCount = res.result;
    })
  }

  getStartDate() {
    this.singleSwitchService.getStartDate().subscribe(res => {
      res.result = new Date(res.result)
      res.result.setHours(res.result.getHours() + 23);
      this.topoStartDate = res.result
      console.log(this.topoStartDate);
      this.startAndNowDate();
    })
  }

  getSystemStatus() {
    this.singleSwitchService.getSystemStatus().subscribe(res => {
      this.systemStatus = res.result;
      if (this.systemStatus) {
        this.getHostCount();
        this.getSwitchCount();
        this.getLinksCount();
        this.getStartDate();
      }
    })
  }

  startAndNowDate() {
    setInterval(() => {
      if (this.topoStartDate != undefined) {
        let date = new Date(new Date().getTime() - this.topoStartDate.getTime());
        this.upTime = this.dateToString(date)
      }
      console.log("Bu fonksiyon her saniye çağrılıyor!");
      // İşlemlerinizi buraya ekleyebilirsiniz
    }, 1000)

  }

  dateToString(date: Date): string {
    const hours = this.padZero(date.getHours());
    const minutes = this.padZero(date.getMinutes());
    const seconds = this.padZero(date.getSeconds());
  
    return `${hours}:${minutes}:${seconds}`;
  }
  
  padZero(value: number): string {
    return value < 10 ? `0${value}` : `${value}`;
  }

}
