import { Component, OnInit } from '@angular/core';
import { Switch } from 'src/app/model';
import { TopologyService } from 'src/app/services/topology.service';

@Component({
  selector: 'app-switch-list',
  templateUrl: './switch-list.component.html',
  styleUrls: ['./switch-list.component.scss']
})
export class SwitchListComponent  implements OnInit{

  switches:Switch[];

  ngOnInit(): void {
    this.getSwitches()
    
  }

  constructor(private topologyService:TopologyService){

  }

  getSwitches(){
    console.log("sdçafş");
    
    this.topologyService.getSwitches().subscribe(res => {
      this.switches = res.result as Switch[]
      console.log(this.switches);
    })
  }
}
