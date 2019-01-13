import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { ActivatedRoute, Router } from '@angular/router';
import { URL_SERVICE } from '../../constantes';

@Component({
  selector: 'app-vizualizacao',
  templateUrl: './vizualizacao.component.html',
  styleUrls: ['./vizualizacao.component.css']
})
export class VizualizacaoComponent implements OnInit {

  id: string;

  constructor(private auth: AuthService, private route: ActivatedRoute, private router: Router) {
    this.route.params.subscribe(params => {
      this.id = params.id;
    });
  }

  ngOnInit() {
    this.abrirArquivo();
    this.verDetalhes();
  }

  private verDetalhes() {
    const url = `detail/${this.id}`;
    this.router.navigateByUrl(url);
  }

  private abrirArquivo() {
    const url = `${URL_SERVICE}/download/${this.auth.getToken()}/${this.id}`;
    window.open(url);
  }
}
