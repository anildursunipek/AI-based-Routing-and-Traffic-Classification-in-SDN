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
import { SelectButtonModule } from 'primeng/selectbutton';
import { FormsModule } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { InputNumberModule } from 'primeng/inputnumber';
import { ButtonModule } from 'primeng/button';
import { HttpClientModule } from  '@angular/common/http';
import { TrafficGenerateComponent } from './components/traffic-generate/traffic-generate.component';
import { DynamicTimePipe } from './pipe/dynamic-time.pipe';

@NgModule({
  declarations: [
    AppComponent,
    SplashScreenComponent,
    DashboardComponent,
    HostListComponent,
    MenuComponent,
    SwitchListComponent,
    LinkListComponent,
    TrafficGenerateComponent,
    DynamicTimePipe
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ProgressSpinnerModule,
    TableModule,
    MenuModule,
    BrowserAnimationsModule,
    SelectButtonModule,
    FormsModule,
    InputTextModule,
    InputNumberModule,
    ButtonModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
