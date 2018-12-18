import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { User } from '../models/user';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class AuthService {

  private BASE_URL = 'http://100.0.66.160:5000/auth';

  private headers: Headers = new Headers({'Content-Type': 'application/json'});

  constructor(private http: Http) {}

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

  ensureAuthenticated(token: string): Promise<any> {
    const url = `${this.BASE_URL}/status`;
    const headers: Headers = new Headers({
      'Content-Type': 'application/json',
      Authorization: `${token}`
    });
    return this.http.get(url, {headers: headers}).toPromise();
  }
}
