import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-detalhe',
  templateUrl: './detalhe.component.html',
  styleUrls: ['./detalhe.component.css']
})
export class DetalheComponent implements OnInit {

  arquivo: any = {};
  id: string;

  constructor(private auth: AuthService, private route: ActivatedRoute, private router: Router) {
    this.route.params.subscribe(params => {
      this.id = params.id;
    });
  }

  ngOnInit() {
    if (this.id) {
      this.carregarDetalhes();
    }
  }

  carregarDetalhes(): any {
    this.auth.ensureAuthenticatedGet(`detail/${this.id}`)
    .then((response) => {
      this.arquivo = response.json().arquivo;
    });
  }

  private visualizar(id) {
    this.router.navigateByUrl(`view/${id}`);
  }
}
