import { Component, OnInit } from '@angular/core';
import { TopologyService } from 'src/app/services/topology.service';

@Component({
  selector: 'app-traffic-generate',
  templateUrl: './traffic-generate.component.html',
  styleUrls: ['./traffic-generate.component.scss']
})
export class TrafficGenerateComponent implements OnInit {

  traffics: any[] = new Array();
  trafficDisable: boolean = false;

  ngOnInit(): void {
    this.getTraffic()
  }

  constructor(private topologyService: TopologyService) {

  }

  startTraffic() {
    this.trafficDisable = true
    this.topologyService.generateTraffic().subscribe(res => {
      this.getTraffic()
    })
  }

  getTraffic() {
    this.trafficDisable = false
    this.topologyService.getTraffic().subscribe(res => {
      this.traffics = res.result;
      if (res.result.length != 0) {
        this.trafficDisable = true
      }
      console.log(res);
    })
  }

  startAndNowDate(second: number, startDate: Date) {

    setInterval(() => {
      const currentDate = new Date();
      const startTime = new Date(startDate).getTime() / 1000; // Başlangıç tarihini saniyeye çevir
  
      // Şu anki tarihi saniyeye çevir ve başlangıç tarihinden çıkart
      const remainingSeconds = Math.floor(startTime + second - currentDate.getTime() / 1000);
      return remainingSeconds
    }, 1000)
  }

}