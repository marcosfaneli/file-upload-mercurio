import { Component, OnInit, Input } from '@angular/core';

declare var $: any;

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {

  @Input() logado = false;

  constructor() {
  }

  ngOnInit() {
  }

  toogleMenu() {
    $('#button-sidebar').click();
    console.log('teste');
  }
}
