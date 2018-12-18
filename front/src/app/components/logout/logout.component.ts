import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})
export class LogoutComponent implements OnInit {

  constructor(private auth: AuthService, private router: Router) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    this.auth.logout(token)
    .catch((err) => {
      console.error(err);
      this.router.navigateByUrl('/')
    });

    localStorage.removeItem('token');
    this.router.navigateByUrl('/login')
  }

}
