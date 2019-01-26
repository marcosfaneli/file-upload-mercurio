import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-request',
  templateUrl: './request.component.html',
  styleUrls: ['./request.component.css']
})
export class RequestComponent implements OnInit {

  carregando = true;
  loading = false;
  error = false;
  error_message = '';
  solicitacoes = [];

  constructor(private auth: AuthService) { }

  ngOnInit() {
    this.carregarSolicitacoes();
  }

  private carregarSolicitacoes() {
    this.auth.ensureAuthenticatedGet('auth/requests')
      .then(res => {
        this.solicitacoes = res.json().solicitacoes;
        this.carregando = false;
      })
      .catch(err => {
        this.carregando = false;
        this.error = true;
        this.error_message = err.message;
      });
  }

  confirmar(id) {
    console.log(id);
    this.loading = true;

    const req = {'id': id };

    this.auth.ensureAuthenticatedPost('auth/accept_register', req)
      .then(res => {
        this.loading = false;
        this.carregarSolicitacoes();
      })
      .catch(err => {
        this.loading = false;
        this.error = true;
        this.error_message = err.json().message;
      });
  }
}
