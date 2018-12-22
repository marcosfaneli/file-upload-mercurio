import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';
import { Arquivo } from '../../models/arquivo';
import { URL_SERVICE } from '../../constantes';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit {

  private arquivo = new Arquivo('', 0, [], '');
  private file: any;

  private BASE_URL = `${URL_SERVICE}/upload`;

  constructor(private http: Http) { }

  ngOnInit() { }

  inputFileChange(event) {
    if (event.target.files && event.target.files[0]) {
      console.log('aqui');
      this.file = event.target.files[0];
    }
  }

  onSubmit(){
    const formData = new FormData();
    formData.append('file', this.file);

    this.http.post(this.BASE_URL, formData)
      .subscribe(resposta => console.log('OK'));
  }

}
