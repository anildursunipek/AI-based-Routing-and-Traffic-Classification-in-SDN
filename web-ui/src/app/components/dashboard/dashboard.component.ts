import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Switch, Host } from 'src/app/model';
import { TopologyService } from 'src/app/services/topology.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  value: string;

  hostCount: number;
  switchCount: number;
  linkCount: number;

  switchDisable: boolean = false;
  hostDisable: boolean = false;
  stopTopoDisable: boolean = false;
  systemStatus: boolean;

  topoStartDate: Date;
  upTime: string = "00:00:00";

  paymentOptions: any[] = [
    { name: 'Topology (Single)', value: "SINGLE_SWITCH_TOPO" },
  ];
  constructor(private router: Router, private topologyService: TopologyService) {

  }

  ngOnInit(): void {
    this.getSystemStatus();

  }

  startSingleSwitchTopo() {
    this.topologyService.topologyStart().subscribe(res => {
      console.log(res);
      this.getSystemStatus();
    }, err => {
      // err
    })
  }

  getHostCount() {
    this.topologyService.getHostsCount().subscribe(res => {
      this.hostCount = res.result;
    })
  }

  getSwitchCount() {
    this.topologyService.getSwitchsCount().subscribe(res => {
      this.switchCount = res.result;
    })
  }

  getLinksCount() {
    this.topologyService.getLinksCount().subscribe(res => {
      this.linkCount = res.result;
    })
  }

  getStartDate() {
    this.topologyService.getStartDate().subscribe(res => {
      res.result = new Date(res.result)
      res.result.setHours(res.result.getHours());
      this.topoStartDate = res.result
      console.log(this.topoStartDate);
      this.startAndNowDate();
    })
  }

  getSystemStatus() {
    this.topologyService.getSystemStatus().subscribe(res => {
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

  stopTopology() {
    this.stopTopoDisable = true
    this.topologyService.topologyStop().subscribe(res => {
      this.hostCount = undefined
      this.switchCount = undefined
      this.linkCount = undefined
      this.topoStartDate = undefined

      this.switchDisable = false;
      this.hostDisable = false;
      this.systemStatus = false;

      this.upTime = "00:00:00"
      setTimeout(() => {
        this.router.navigate(['/']);
      }, 3000);

    })
  }
}