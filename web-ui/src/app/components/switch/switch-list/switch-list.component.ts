import { Component, OnInit } from '@angular/core';
import { Switch } from 'src/app/model';
import { SingleSwitchService } from 'src/app/services/single-switch.service';

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

  constructor(private singleSwitchService:SingleSwitchService){

  }

  getSwitches(){
    console.log("sdçafş");
    
    this.singleSwitchService.getSwitches().subscribe(res => {
      this.switches = res.result as Switch[]
      console.log(this.switches);
    })
  }
}
