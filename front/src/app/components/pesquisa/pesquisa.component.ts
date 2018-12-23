import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-pesquisa',
  templateUrl: './pesquisa.component.html',
  styleUrls: ['./pesquisa.component.css']
})
export class PesquisaComponent implements OnInit {

  arquivos: any[] = [];
  texto: string;

  constructor(private auth: AuthService, private route: ActivatedRoute) {
    this.route.params.subscribe(params => {
      this.texto = params.texto;
    });
  }

  ngOnInit() {
    if (this.texto) {
      this.buscarArquivos();
    }
  }

  private buscarArquivos() {
    if (this.texto) {
      this.auth.ensureAuthenticatedGet(`pesquisa/${this.texto}`)
        .then((response) => {
          this.arquivos = response.json().arquivos;
        });
    }
  }
}
