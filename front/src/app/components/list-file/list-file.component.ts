import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-list-file',
  templateUrl: './list-file.component.html',
  styleUrls: ['./list-file.component.css']
})
export class ListFileComponent implements OnInit {

  _arquivos: any[];

  constructor() { }

  ngOnInit() { }

  @Input()
  set arquivos(lista: any[]){
    this._arquivos = lista;
  }

  get arquivos(): any[]{
    return this._arquivos;
  }

}
