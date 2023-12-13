import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { TopologyService } from 'src/app/services/topology.service';

@Component({
  selector: 'app-splash-screen',
  templateUrl: './splash-screen.component.html',
  styleUrls: ['./splash-screen.component.scss']
})
export class SplashScreenComponent {

  flag:boolean = true

  ngOnInit(): void {
  }

  constructor(private router: Router, private topologyService:TopologyService) {

  }

  startTopology(){
    this.flag = false
    this.topologyService.topologyStart().subscribe(res => {
      this.router.navigate(['/dashboard']);
    })
  }
}