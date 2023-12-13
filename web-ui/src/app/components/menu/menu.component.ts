import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss']
})
export class MenuComponent implements OnInit{
  items: MenuItem[] | undefined;

  ngOnInit() {
      this.items = [
          {
              label: 'Controller (Home)',
              icon: 'pi pi-home',
              routerLink: 'dashboard'
          },
          {
              label: 'Switches',
              icon: 'pi pi-sync',
              routerLink: 'switch/list'

          },
          {
              label: 'Hosts',
              icon: 'pi pi-desktop',
              routerLink: 'host/list'
          },
          {
              label: 'Links',
              icon: 'pi pi-compass',
              routerLink:"link/list"
          },
          {
              label: 'Topology',
              icon: 'pi pi-slack',
              routerLink: "topology/graph"
          },
          {
              label: 'Firewall',
              icon: 'pi pi-exclamation-triangle'
          },
          {
              label: 'Access Control Lists',
              icon: 'pi pi-exclamation-triangle'
          },
          {
              label: 'Statistics',
              icon: 'pi pi-chart-bar'
          },
          {
              label: 'Change Controllers',
              icon: 'pi pi-chevron-circle-right'
          }
      ];
  }
}
