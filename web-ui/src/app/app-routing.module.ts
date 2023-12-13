import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SplashScreenComponent } from './components/splash-screen/splash-screen.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { HostListComponent } from './components/host/host-list/host-list.component';
import { SwitchListComponent } from './components/switch/switch-list/switch-list.component';
import { LinkListComponent } from './components/link/link-list/link-list.component';
import { TrafficGenerateComponent } from './components/traffic-generate/traffic-generate.component';

const routes: Routes = [
  {path: '', component: SplashScreenComponent},
  {path: 'dashboard', component: DashboardComponent},
  {path: 'host/list', component: HostListComponent},
  {path: 'switch/list', component: SwitchListComponent},
  {path: 'link/list', component: LinkListComponent},
  {path: 'traffic/generate', component: TrafficGenerateComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
