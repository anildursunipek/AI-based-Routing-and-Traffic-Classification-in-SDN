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
          },
          {
              label: 'Switches',
              icon: 'pi pi-sync'
          },
          {
              label: 'Hosts',
              icon: 'pi pi-desktop'
          },
          {
              label: 'Links',
              icon: 'pi pi-compass'
          },
          {
              label: 'Topology',
              icon: 'pi pi-slack'
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
