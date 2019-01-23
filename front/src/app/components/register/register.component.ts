import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { Solicitacao } from '../../models/request';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {

  loading = false;
  error = false;
  error_message = '';
  solicitacao: Solicitacao = new Solicitacao();

  constructor(private auth: AuthService, private router: Router) {}

  onRegister() {
    this.loading = true;

    this.auth.register(this.solicitacao)
    .then((user) => {
      this.router.navigateByUrl('/login');
    })
    .catch((err) => {
      this.loading = false;
      this.error = true;
      this.error_message = err.json().message;
      console.log(err);
    });
  }
}
