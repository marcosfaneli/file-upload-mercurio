import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { User } from '../../models/user';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {

  user: User = new User();

  constructor(private auth: AuthService, private router: Router) {}

  onRegister(): void {
    this.auth.register(this.user)
    .then((user) => {
      this.router.navigateByUrl('/login');
    })
    .catch((err) => {
      console.log(err);
    });
  }
}
