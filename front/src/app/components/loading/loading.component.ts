import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-loading',
  template: '<h5 *ngIf="exibir" class="text-center" style="color: #ccc; margin-top: 12px;"><i class="fa fa-spinner fa-spin fa-fw"></i> Carregando...</h5>',
  styleUrls: ['./loading.component.css']
})
export class LoadingComponent implements OnInit {

  @Input() exibir = false;

  constructor() { }

  ngOnInit() {
  }

}
