import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit {
  form: FormGroup;
  loading = false;
  error = false;
  error_message = '';
  categorias = [];

  @ViewChild('fileInput') fileInput: ElementRef;

  constructor(private fb: FormBuilder, private auth: AuthService, private router: Router) {
    this.createForm();
  }

  ngOnInit() {
    this.carregarCategorias();
  }

  carregarCategorias(): any {
    this.auth.ensureAuthenticatedGet('categoria')
      .then(resposta => {
        this.categorias = resposta.json().categorias;
      });
  }

  createForm() {
    this.form = this.fb.group({
      descricao: ['', Validators.required],
      chave: ['', Validators.required],
      categoria: ['', Validators.required],
      arquivo: null
    });
  }

  onFileChange(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.form.get('arquivo').setValue(file);
    }
  }

  private prepareSave(): any {
    const input = new FormData();
    input.append('descricao', this.form.get('descricao').value);
    input.append('arquivo', this.form.get('arquivo').value);
    input.append('chave', this.form.get('chave').value);
    input.append('categoria', this.form.get('categoria').value);
    return input;
  }

  onSubmit() {
    const formModel = this.prepareSave();
    this.loading = true;

    this.auth.ensureAuthenticatedUpload('upload', formModel)
      .then(resposta => {
        if (resposta.json().success === true) {
          this.router.navigateByUrl(`view/${resposta.json().id}`);
        }
      })
      .catch((err) => {
        this.loading = false;
        this.error = true;
        this.error_message = err.json().message;
      });
  }

  clearFile() {
    this.form.get('arquivo').setValue(null);
    this.fileInput.nativeElement.value = '';
  }
}
