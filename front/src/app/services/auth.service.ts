import { Injectable } from '@angular/core';
import { Headers, Http, RequestOptions } from '@angular/http';
import { User } from '../models/user';
import { Router } from '@angular/router';
import 'rxjs/add/operator/toPromise';
import { URL_SERVICE } from '../constantes';

@Injectable()
export class AuthService {

  private BASE_URL = `${URL_SERVICE}/auth`;

  private headers: Headers = new Headers({'Content-Type': 'application/json'});

  constructor(private http: Http, private router: Router) {}

  private getToken(): string {
    return localStorage.getItem('token');
  }

  logout(token: string): Promise<any> {
    const url = `${this.BASE_URL}/logout`;
    const headers: Headers = new Headers({
      'Content-Type': 'application/json',
      Authorization: `${token}`
    });
    return this.http.get(url, {headers: headers}).toPromise();
  }

  login(user: User): Promise<any> {
    const url = `${this.BASE_URL}/login`;
    return this.http.post(url, user, {headers: this.headers}).toPromise();
  }

  register(user: User): Promise<any> {
    const url = `${this.BASE_URL}/register`;
    return this.http.post(url, user, {headers: this.headers}).toPromise();
  }

  ensureAuthenticatedGet(route: string): Promise<any> {
    const token = localStorage.getItem('token');

    const url = this.getUrl(route);

    const headers: Headers = new Headers({
      'Content-Type': 'application/json',
      Authorization: `${this.getToken()}`
    });
    return this.http.get(url, {headers: headers})
      .toPromise()
      .catch((err) => {
        console.error(err);
        this.router.navigateByUrl('/logout');
      });
  }

  ensureAuthenticatedPost(route: string, payload: any): Promise<any> {

    const token = localStorage.getItem('token');

    const url = this.getUrl(route);

    const headers: Headers = new Headers({
      'Content-Type': 'application/json',
      Authorization: `${this.getToken()}`
    });

    return this.http.post(url, payload, {headers: headers})
      .toPromise()
      .catch((err) => {
        console.error(err);
        this.router.navigateByUrl('/logout');
      });
  }
  getUrl(route: string): any {
    return `${URL_SERVICE}/${route}`;
  }

  ensureAuthenticatedUpload(route: string, formData: FormData): Promise<any> {

    const headers = new Headers();
    headers.append('Accept', 'application/json');
    headers.append('Authorization', `${this.getToken()}`);

    const options = new RequestOptions({ headers: headers });

    return this.http.post(`${this.getUrl(route)}`, formData, options)
      .toPromise()
      .catch((err) => {
        console.error(err);
        this.router.navigateByUrl('/logout');
      });
  }
}
