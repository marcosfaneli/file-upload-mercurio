import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-list-file',
  templateUrl: './list-file.component.html',
  styleUrls: ['./list-file.component.css']
})
export class ListFileComponent implements OnInit {

  _arquivos: any[] = [];

  constructor(private router: Router) { }

  ngOnInit() { }

  @Input()
  set arquivos(lista: any[]){
    this._arquivos = lista;
  }

  get arquivos(): any[]{
    return this._arquivos;
  }

  private detalhes(id) {
    this.router.navigateByUrl(`detail/${id}`);
  }

  private visualizar(id) {
    this.router.navigateByUrl(`view/${id}`);
  }

}
