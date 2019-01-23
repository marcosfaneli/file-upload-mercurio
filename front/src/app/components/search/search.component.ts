import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class PesquisaComponent implements OnInit {

  arquivos: any[] = [];
  texto: string;
  loading = false;
  carregando = true;
  error = false;
  error_message = '';
  quantidadeBuscas = 0;

  constructor(private auth: AuthService, private route: ActivatedRoute) {
    this.route.params.subscribe(params => {
      this.texto = params.text;
    });
  }

  ngOnInit() {
    if (this.texto) {
      this.buscarArquivos();
    }
  }

  private buscarArquivos() {
    this.loading = true;
    if (this.texto) {
      this.auth.ensureAuthenticatedGet(`find/${this.texto}`)
        .then((response) => {
          this.loading = false;
          this.quantidadeBuscas++;
          this.arquivos = response.json().arquivos;
        })
        .catch(err => {
          this.carregando = false;
          this.error = true;
          this.error_message = err.message;
        });
    }
  }
}
