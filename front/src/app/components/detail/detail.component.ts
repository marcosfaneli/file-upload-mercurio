import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.css']
})
export class DetalheComponent implements OnInit {

  arquivo: any = {};
  id: string;
  error = false;
  error_message = '';
  carregando = true;

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
      this.carregando = false;
    })
    .catch(err => {
      this.error = true;
      this.error_message = err.message;
      console.error(err);
    });
  }

  private visualizar(id) {
    this.router.navigateByUrl(`view/${id}`);
  }
}
