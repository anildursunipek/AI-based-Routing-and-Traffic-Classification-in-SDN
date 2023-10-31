import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SplashScreenComponent } from './components/splash-screen/splash-screen.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { HostListComponent } from './components/host/host-list/host-list.component';
import { SwitchListComponent } from './components/switch/switch-list/switch-list.component';

const routes: Routes = [
  {path: '', component: SplashScreenComponent},
  {path: 'dashboard', component: DashboardComponent},
  {path: 'host/list', component: HostListComponent},
  {path: 'switch/list', component: SwitchListComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
