import { Component, OnInit } from '@angular/core';
import { Host } from 'src/app/model';
import { SingleSwitchService } from 'src/app/services/single-switch.service';

@Component({
  selector: 'app-host-list',
  templateUrl: './host-list.component.html',
  styleUrls: ['./host-list.component.scss']
})
export class HostListComponent implements OnInit {

  hosts:Host[];

  ngOnInit(): void {
    this.getHosts()
    
  }

  constructor(private singleSwitchService:SingleSwitchService){

  }

  getHosts(){
    this.singleSwitchService.getHosts().subscribe(res => {
      this.hosts = res.result as Host[]
      console.log(this.hosts);
    })
  }

}
