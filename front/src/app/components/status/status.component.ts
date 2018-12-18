import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-status',
  templateUrl: './status.component.html',
  styleUrls: ['./status.component.css']
})
export class StatusComponent implements OnInit {

  isLoggedIn: boolean = false;

  constructor(private auth: AuthService, private router: Router) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.auth.ensureAuthenticated(token)
      .then((user) => {
        if (user.json().success === true) {
          this.isLoggedIn = true;
        }
      })
      .catch((err) => {
        console.error(err);
        this.router.navigateByUrl('/logout')
      });
    }
  }

}
