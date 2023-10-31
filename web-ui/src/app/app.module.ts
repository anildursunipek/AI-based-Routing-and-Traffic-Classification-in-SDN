import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SplashScreenComponent } from './components/splash-screen/splash-screen.component';
import { ProgressSpinnerModule } from 'primeng/progressspinner';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { HostListComponent } from './components/host/host-list/host-list.component';
import { TableModule } from 'primeng/table';
import { MenuComponent } from './components/menu/menu.component';
import { MenuModule } from 'primeng/menu';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { SwitchListComponent } from './components/switch/switch-list/switch-list.component';
import { LinkListComponent } from './components/link/link-list/link-list.component';

@NgModule({
  declarations: [
    AppComponent,
    SplashScreenComponent,
    DashboardComponent,
    HostListComponent,
    MenuComponent,
    SwitchListComponent,
    LinkListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ProgressSpinnerModule,
    TableModule,
    MenuModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
