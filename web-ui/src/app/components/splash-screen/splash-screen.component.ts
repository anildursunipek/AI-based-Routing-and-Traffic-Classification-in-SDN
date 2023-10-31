import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-splash-screen',
  templateUrl: './splash-screen.component.html',
  styleUrls: ['./splash-screen.component.scss']
})
export class SplashScreenComponent {

  ngOnInit(): void {
  }

  constructor(private router: Router) {

  }

  closeSplash() {
    var splash = document.getElementById('splash')!;
    splash.classList.add('hidden');
  
    // Belirlediğin animasyon süresi kadar bekleyip sonra splash'ı tamamen gizle
    setTimeout(() => {
      splash.style.display = 'none';
      this.router.navigate(['/dashboard']);
    }, 3000);
  }
}
