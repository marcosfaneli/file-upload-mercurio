import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit {

  constructor(private http: Http) { }

  ngOnInit() {
  }

  inputFileChange(event) {
    if (event.target.files && event.target.files[0]) {
      console.log('aqui');
      const file = event.target.files[0];
      const formData = new FormData();
      formData.append('file', file);

      this.http.post('http://100.0.66.160:5000/upload', formData)
        .subscribe(resposta => console.log('OK'));
    }
  }

}
