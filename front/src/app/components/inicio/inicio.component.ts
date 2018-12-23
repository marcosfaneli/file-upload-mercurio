import { Component, OnInit } from '@angular/core';

import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-inicio',
  templateUrl: './inicio.component.html',
  styleUrls: ['./inicio.component.css']
})
export class InicioComponent implements OnInit {

  texto: string;

  categorias: any[];
  arquivos: any[];

  constructor(private auth: AuthService) { }

  ngOnInit() {
    this.carregarCategorias();
    this.carregarArquivos();
  }

  private carregarCategorias() {
    this.auth.ensureAuthenticatedGet('categoria')
      .then((response) => {
        this.categorias = response.json().categorias;
      });
  }

  private carregarArquivos() {
    this.auth.ensureAuthenticatedGet('recente')
      .then((response) => {
        this.arquivos = response.json().arquivos;
      });
  }
}
