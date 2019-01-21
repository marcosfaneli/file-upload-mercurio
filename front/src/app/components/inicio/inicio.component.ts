import { Component, OnInit } from '@angular/core';

import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-inicio',
  templateUrl: './inicio.component.html',
  styleUrls: ['./inicio.component.css']
})
export class InicioComponent implements OnInit {

  carregando = true;
  profile: any;

  categorias: any[];
  arquivos: any[];

  constructor(private auth: AuthService) { }

  ngOnInit() {
    this.carregarProfile();
    this.carregarCategorias();
    this.carregarArquivos();
  }
  carregarProfile(): any {
    this.auth.ensureAuthenticatedGet('status')
      .then((response) => {
        this.profile = response.json().profile;
      });
  }

  private carregarCategorias() {
    this.auth.ensureAuthenticatedGet('categoria')
      .then((response) => {
        this.categorias = response.json().categorias;
      });
  }

  private carregarArquivos() {
    this.auth.ensureAuthenticatedGet('recent')
      .then((response) => {
        this.arquivos = response.json().arquivos;
        this.carregando = false;
      });
  }
}
