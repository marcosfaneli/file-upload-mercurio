import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';
import { URL_SERVICE } from '../../constantes';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit {

  private arquivo: any = {};
  private file: any;
  private categorias = [];

  constructor(private auth: AuthService) { }

  ngOnInit() {
    this.carregarCategorias();
  }

  private carregarCategorias() {
    this.auth.ensureAuthenticatedGet('categoria')
      .then((response) => {
        this.categorias = response.json().categorias;
      });
  }

  inputFileChange(event) {
    if (event.target.files && event.target.files[0]) {
      console.log('aqui');
      this.file = event.target.files[0];
    }
  }

  onSubmit() {
    const formData = new FormData();
    formData.append('file', this.file);
    formData.append('categoria', this.arquivo.categoria);
    formData.append('descricao', this.arquivo.descricao);
    formData.append('chave', this.arquivo.chave);

    this.auth.ensureAuthenticatedPost('upload', formData)
      .then(resposta => console.log('OK'));
  }

}
