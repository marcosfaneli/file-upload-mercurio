import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

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

  constructor(private auth: AuthService, private route: Router) { }

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
    this.auth.ensureAuthenticatedGet('arquivo')
      .then((response) => {
        this.arquivos = response.json().arquivos;
      });
  }

  private buscarArquivos() {
    this.route.navigateByUrl(`pesquisa/${this.texto}`);
  }
}
