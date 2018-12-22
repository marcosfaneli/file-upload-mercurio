import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { User } from '../../models/user';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  user: User = new User();

  error = false;

  constructor(private auth: AuthService, private router: Router) { }

  onLogin(): void {
    this.auth.login(this.user)
    .then((user) => {
      const token = user.json().token;

      localStorage.setItem('token', token);

      this.router.navigateByUrl('/');
    })
    .catch((err) => {
      this.error = true;
      console.log(err);
    });
  }

  closeAlert() {
    this.error = false;
  }
}
